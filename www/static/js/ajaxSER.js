// vid
const sers = document.querySelectorAll('.item');
const deleteButton = document.getElementById('deleteButton');
const updateButton = document.getElementById('updateButton');
let selectedSerlId = null;

  
sers.forEach(seria => {
    seria.addEventListener('click', () => {
        sers.forEach(seria => {
            seria.classList.remove('selected');
        });
        deleteButton.disabled = false;
        updateButton.disabled = false;
        deleteButton.classList.remove('desable');
        updateButton.classList.remove('desable');

        seria.classList.add('selected');   
        selectedSerlId = seria.dataset.id;
    
    });
        
    document.addEventListener('click', function(event) {
        const target = event.target;
        if (!event.target.closest('.item')) {
            deleteButton.disabled = true;
            updateButton.disabled = true;
            deleteButton.classList.add('desable');
            updateButton.classList.add('desable');
    
            seria.classList.remove('selected');  

        }
    });
       
});

// Delete
deleteButton.addEventListener('click', () => {
    const action = confirm('Подтвердите удаление путевого листа с номером '+ `${selectedSerlId}`);
    if (action) {
      $.ajax({
        url: '/ajax/delete8/',
        data: {
          'id': selectedSerlId,
        },
        dataType: 'json',
        success: function (data) {
          if (data.deleted) {
            $('.item[data-id=' + selectedSerlId + ']').remove();
            selectedSerlId = null;
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
    url: `update/${selectedSerlId}/`,
    data: {
      'id': selectedSerlId,
      'csrfmiddlewaretoken': csrf_token,
    },
    dataType: 'html',
    type: 'POST',
    success: function() { // Добавляем функцию success для обработки ответа
      window.location.href = `update/${selectedSerlId}/`;

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