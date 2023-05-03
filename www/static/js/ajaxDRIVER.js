// vid
const drivers = document.querySelectorAll('.item');
const deleteButton = document.getElementById('deleteButton');
const updateButton = document.getElementById('updateButton');
let selectedDriverId = null;

  
drivers.forEach(driver => {
    driver.addEventListener('click', () => {
        drivers.forEach(driver => {
            driver.classList.remove('selected');
        });
        deleteButton.disabled = false;
        updateButton.disabled = false;
        deleteButton.classList.remove('desable');
        updateButton.classList.remove('desable');


        driver.classList.add('selected');   
        selectedDriverId = driver.dataset.id;
    
    });
        
    document.addEventListener('click', function(event) {
        const target = event.target;
        if (!event.target.closest('.item')) {
            deleteButton.disabled = true;
            updateButton.disabled = true;
            deleteButton.classList.add('desable');
            updateButton.classList.add('desable');
    
            driver.classList.remove('selected');  

        }
    });
       
});

// Delete
deleteButton.addEventListener('click', () => {
    const action = confirm('Подтвердите удаление путевого листа с номером '+ `${selectedDriverId}`);
    if (action) {
      $.ajax({
        url: '/ajax/delete3/',
        data: {
          'id': selectedDriverId,
        },
        dataType: 'json',
        success: function (data) {
          if (data.deleted) {
            $('.item[data-id=' + selectedDriverId + ']').remove();
            selectedDriverId = null;
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
    url: `update/${selectedDriverId}/`,
    data: {
      'id': selectedDriverId,
      'csrfmiddlewaretoken': csrf_token,
    },
    dataType: 'html',
    type: 'POST',
    success: function() { // Добавляем функцию success для обработки ответа
      window.location.href = `update/${selectedDriverId}/`;

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