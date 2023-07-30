import random
from django.http import JsonResponse
from django.shortcuts import render
from .models import *
from django.views.decorators.csrf import csrf_exempt



def index(request):
    template = 'main/index.html'
    return render(request, template)


# 
def lusher_recieve_result(request):
    
    if request.method == "POST":
        result = request.POST.get('result', None)
        print('result - ', result)

        if result is not None:
            try:
                lusher_result = Lusher_results.objects.create(result=result)
                lusher_result.save()
                return JsonResponse({'success': True})
            except Exception as e:
                return JsonResponse({'success': False, 'error': str(e)})
            
        

    return JsonResponse({'success': False, 'error': 'Invalid data'})

# @csrf_exempt
def get_interpretation_result(request):
    # if request.method == "POST":
    # color_combination = request.GET.get('color')
    # color_combination = ["green", "blue"]
    data = {
        'green' : 'green',
        }

        # if color_combination:
        #     # Получаем интерпретации из таблицы LusherColorPair для заданной комбинации цветов
        #     interpretations = []
        #     for i in range(len(color_combination)):
        #         for j in range(i + 1, len(color_combination)):
        #             color_pair = color_combination[i] + ' ' + color_combination[j]
        #             try:
        #                 pair_obj = LusherColorPair.objects.get(color_pair=color_pair)
        #                 interpretations.append(pair_obj.interpretation)
        #             except LusherColorPair.DoesNotExist:
        #                 pass  # Интерпретация для этой пары отсутствует, пропускаем

        #     # Формируем список интерпретаций из LusherColorPair
        #     interpretations_list = interpretations

        #     return JsonResponse({'success': True, 'interpretations': interpretations_list})

    # return JsonResponse({'success': False, 'error': 'Invalid data'})
    return JsonResponse(data)


def interpret_luscher_results(colors_array):
    # Словарь, где ключ - цвет, значение - характеристики
    color_characteristics = {
        'green': 'Спокойствие, удовлетворение, умиротворение, чувство уверенности, настойчивость, иногда упрямство,',
        'blue': 'Сосредоточенность, вдумчивость, расслабление, спокойствие, удовлетворенность,',
        'red': 'Энергия, возбуждение, стресс, символизирует силу волевого усилия, агрессивность, наступательные тенденции, возбуждение,',
        'yellow': 'активность, стремление к общению, экспансивность, веселость',
        'violet': 'тревожность, стресс, переживание страха, огорчения',
        'broun': '',
        'black': '',
        'gray': '',
        # Добавьте другие цвета и характеристики по необходимости
    }

    plus_colors = []
    minus_colors = []

    for color in colors_array:
        if color in color_characteristics:
            # Здесь можно добавить логику, чтобы определить, что считать плюсом или минусом.
            # Например, можно разделить цвета на плюсы и минусы по их характеристикам.
            # В данном примере я просто случайным образом разделю цвета на плюсы и минусы.
            if random.random() < 0.5:
                plus_colors.append(color)
            else:
                minus_colors.append(color)

    interpretation = {
        'plus_colors': plus_colors,
        'minus_colors': minus_colors,
        'characteristics': {
            'plus': [color_characteristics[color] for color in plus_colors],
            'minus': [color_characteristics[color] for color in minus_colors]
        }
    }

    return interpretation
