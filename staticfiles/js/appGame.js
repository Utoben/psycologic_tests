
symbolArray=[];

$(document).ready(function() {
    $(".res").click(function() {
      var symbol = $(this).data("symbol");
      $("#symbolList").append("<li>" + symbol + "</li>");
      symbolArray.push(symbol); // Добавляем символ в массив
      updateSymbolList(); // Обновляем список символов
    });
  });
  
  function updateSymbolList() {
    $("#symbolList").empty(); // Очищаем список

    for (var i = 0; i < symbolArray.length; i++) {
      var symbol = symbolArray[i];
      $("#symbolList").append("<li>" + symbol + "</li>"); // Добавляем символ в список
    }

    // Обновляем значение скрытого поля при каждом изменении массива
    $("#resultInput").val(symbolArray.join(','));
  }

  function sendResult(event) {
    event.preventDefault();
    // var laborCostId = currentLaborCostId;
    // var csrfToken = $('#editForm input[name="csrfmiddlewaretoken"]').val();
    
    // var result = symbolArray;
    // console.log('res= ', result)
    var formData = $('#editForm').serialize();

      $.ajax({
          url: '/lusher_results/',
          type: 'POST',
          data: formData,
        
          success: function(response) {
              // Обработка успешного обновления записи
              
              // location.reload();
              console.log("success", formData)
          },
          error: function(xhr, status, error) {
              // Обработка ошибки
              console.log("No success")
          }
      });
  }

  $(document).ready(function() {
    // Найти кнопку отправки
    var submitButton = document.getElementById('lusher_send');
    
    submitButton.addEventListener('click', function(){
      sendResult(event);
    });
   
  });
  
  