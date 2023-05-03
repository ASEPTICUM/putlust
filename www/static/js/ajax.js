
// Delete-zadan

function Delete(id) {
    var action = confirm("Вы точно хотите удалить?");
    if (action != false) {
      $.ajax({
          url: '/ajax/delete4/',
          data: {
              'id': id,
          },
          dataType: 'json',
          success: function (data) {
              if (data.deleted) {
                $("#TableZadan #zakaz-" + id).remove().draw(false);
              }
          }
      });
      setTimeout(function(){
            location.reload();
        }, 400);
    }
  }


// Delete-TWO
const putlists = document.querySelectorAll('.item');
const tt = document.querySelectorAll('.tt');
const deleteButton = document.getElementById('deleteButton');
const updateButton = document.getElementById('updateButton');
const downloadButton = document.getElementById('downloadButton');
let selectedPutlistId = null;

  
putlists.forEach(putlist => {
    putlist.addEventListener('click', () => {
        putlists.forEach(putlist => {
            putlist.classList.remove('selected');
        });
        deleteButton.disabled = false;
        updateButton.disabled = false;
        downloadButton.disabled = false;
        deleteButton.classList.remove('desable');
        updateButton.classList.remove('desable');
        downloadButton.classList.remove('desable');

        putlist.classList.add('selected');   
        selectedPutlistId = putlist.dataset.id;
    
    });
        
    document.addEventListener('click', function(event) {
        const target = event.target;
        if (!event.target.closest('.item')) {
            deleteButton.disabled = true;
            updateButton.disabled = true;
            downloadButton.disabled = true;
            deleteButton.classList.add('desable');
            updateButton.classList.add('desable');
            downloadButton.classList.add('desable');
      
            putlist.classList.remove('selected');  

        }
    });
       
});

/*$(document).on('click', '.tt', function(event) {
    var $target = $(event.target);
    var recordId = $target.closest('.tt').data('record-id');
    $('.tt[data-record-id="' + recordId + '"]').addClass('sel');
    console.log(recordId);
});*/


deleteButton.addEventListener('click', () => {
    const action = confirm('Подтвердите удаление путевого листа с номером '+ `${selectedPutlistId}`);
    if (action) {
      $.ajax({
        url: '/ajax/delete/',
        data: {
          'id': selectedPutlistId,
        },
        dataType: 'json',
        success: function (data) {
          if (data.deleted) {
            $('.item[data-id=' + selectedPutlistId + ']').remove();
            selectedPutlistId = null;
            deleteButton.disabled = true;
            deleteButton.classList.add('desable');
            refreshPage();
          }
        }
      });
      
    }
});


updateButton.addEventListener('click', () => {
  const csrf_token = $('input[name="csrfmiddlewaretoken"]').val();
  $.ajax({
    url: `update/${selectedPutlistId}/`,
    data: {
      'id': selectedPutlistId,
      'csrfmiddlewaretoken': csrf_token,
    },
    dataType: 'html',
    type: 'POST',
    success: function() { // Добавляем функцию success для обработки ответа
      window.location.href = `update/${selectedPutlistId}/`;

    }
  });
});


downloadButton.addEventListener('click', () => {
  const csrf_token = $('input[name="csrfmiddlewaretoken"]').val();
  $.ajax({
    url: `render_pdf_view/${selectedPutlistId}/`,
    data: {
      'id': selectedPutlistId,
      'csrfmiddlewaretoken': csrf_token,
    },
    dataType: 'html',
    type: 'POST',
    success: function() { // Добавляем функцию success для обработки ответа
      window.location.href = `render_pdf_view/${selectedPutlistId}/`;

    }
  });
});


function refreshPage() {
  var number = window.location.href;
  $.ajax({
    url: '/',
    data: {
      'page_obj': number,
    },
    dataType: 'html',
    success: function (data) {

      $('#body').replaceWith(data);
      // Обновляем ссылки на кнопки удаления, редактирования и т.д.
      updateLinks();
      

    }
  });
}

/*function refreshPage() {
  const pageUrl = window.location.href;

  // Получаем количество записей на странице пагинации.
  const pageCount = 11;

  // Отправляем AJAX-запрос на сервер Django, передавая количество записей на странице.
  $.get(pageUrl, { 'page_count': pageCount }).done(function (data) {
    const pageHtml = $(data).find('#TablePuts');
    $('#TablePuts').replaceWith(pageHtml);
    updateLinks();
  });
}*/




  // Получаем CSRF-токен из cookie
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === `${name}=`) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}