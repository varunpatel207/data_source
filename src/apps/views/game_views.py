import pandas
from django.shortcuts import render
from apps.models.game_data_model import GameData
from apps.models.game_model import Game
from helper.helper import generate_slug, object_as_dict


class GameViews:
    def dashboard(request):
        page = request.GET.get('page') or 0

        if request.POST:
            pass

        game_data_objects, game_data_count = GameData.game_filter(page=page)

        print('game_data_objects')
        print(game_data_objects)

        game_data_dict = {}
        game_dict = {}
        for game_data_object, game_object in game_data_objects:
            game_data_dict[game_data_object.id] = game_data_object
            game_dict[game_object.id] = game_object

            print("game_data_object.game_id", game_data_object.game_id)

        context = {
            'game_data': game_data_dict,
            'game': game_dict
        }
        return render(request, "game/dashboard.html", context)

    def game_info(request):
        slug = request.GET.get('slug')

        game_object = Game.get_by_slug(slug)
        if game_object:
            game_data_objects, count = GameData.search_game(game_id=game_object.id)
            print(game_data_objects)

            game_data_dict = {}
            if game_data_objects:
                for game_data_object in game_data_objects:
                    game_data_dict[game_data_object.id] = object_as_dict(game_data_object)

        context = {
            'game_data': game_data_dict
        }
        return render(request, 'game/game_info.html', context)

    def upload_game_data(request):
        print('in here')

        if request.FILES:
            game_file = request.FILES.get('file')

            dataframe = pandas.read_csv(game_file, index_col=None)
            dataframe.fillna('', inplace=True)

            game_data_list = []
            for row_index, row in enumerate(dataframe.iterrows()):
                game_dict = {}
                for index, value in enumerate(list(row[1])):
                    column_name = dataframe.columns[index]
                    if column_name == "Game":
                        game_slug = generate_slug(value)
                        game_dict['slug'] = game_slug

                    game_dict[column_name.lower()] = value
                game_data_list.append(game_dict)

            if game_data_list:
                for game_dict in game_data_list:
                    slug = game_dict.get('slug')
                    game_object = Game.get_by_slug(slug)
                    if not game_object:
                        game_object = Game()
                        for key in game_dict.keys():
                            if key in ['game', 'slug']:
                                setattr(game_object, key, game_dict[key])
                        game_object.add()
                    game_dict['game_id'] = game_object.id

                    print('game_dict', game_dict)

                game_data_object_list = []
                for game_dict in game_data_list:
                    game_object = GameData()
                    for key, value in game_dict.items():
                        if key == "hours_streamed":
                            value = value.replace('hours', '')
                            value = value.strip()
                        setattr(game_object, key, value)
                    game_data_object_list.append(game_object)

                if game_data_object_list:
                    GameData.bulk_add(game_data_object_list)

        return render(request, "game/upload_game_data.html", {})
