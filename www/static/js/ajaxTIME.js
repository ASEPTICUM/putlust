// vid
const times = document.querySelectorAll('.item');
const deleteButton = document.getElementById('deleteButton');
const updateButton = document.getElementById('updateButton');
let selectedTimelId = null;

  
times.forEach(timeWork => {
    timeWork.addEventListener('click', () => {
        times.forEach(timeWork => {
            timeWork.classList.remove('selected');
        });
        deleteButton.disabled = false;
        updateButton.disabled = false;
        deleteButton.classList.remove('desable');
        updateButton.classList.remove('desable');

        timeWork.classList.add('selected');   
        selectedTimelId = timeWork.dataset.id;
    
    });
        
    document.addEventListener('click', function(event) {
        const target = event.target;
        if (!event.target.closest('.item')) {
            deleteButton.disabled = true;
            updateButton.disabled = true;
            deleteButton.classList.add('desable');
            updateButton.classList.add('desable');
    
            timeWork.classList.remove('selected');  

        }
    });
       
});

// Delete
deleteButton.addEventListener('click', () => {
    const action = confirm('Подтвердите удаление путевого листа с номером '+ `${selectedTimelId}`);
    if (action) {
      $.ajax({
        url: '/ajax/delete7/',
        data: {
          'id': selectedTimelId,
        },
        dataType: 'json',
        success: function (data) {
          if (data.deleted) {
            $('.item[data-id=' + selectedTimelId + ']').remove();
            selectedTimelId = null;
            deleteButton.disabled = true;
            deleteButton.classList.add('desable');
          }
        }
      });
      
    }
});

// Update
updateButton.addEventListener('click', () => {
  const csrf_token = $('input[name="csrfmiddlewaretoken"]').val();
  $.ajax({
    url: `update/${selectedToplId}/`,
    data: {
      'id': selectedToplId,
      'csrfmiddlewaretoken': csrf_token,
    },
    dataType: 'html',
    type: 'POST',
    success: function() { // Добавляем функцию success для обработки ответа
      window.location.href = `update/${selectedToplId}/`;

    }
  });
});




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