// vid
const cars = document.querySelectorAll('.item');
const deleteButton = document.getElementById('deleteButton');
const updateButton = document.getElementById('updateButton');
let selectedCarId = null;

  
cars.forEach(car => {
    car.addEventListener('click', () => {
        cars.forEach(car => {
            car.classList.remove('selected');
        });
        deleteButton.disabled = false;
        updateButton.disabled = false;
        deleteButton.classList.remove('desable');
        updateButton.classList.remove('desable');


        car.classList.add('selected');   
        selectedCarId = car.dataset.id;
    
    });
        
    document.addEventListener('click', function(event) {
        const target = event.target;
        if (!event.target.closest('.item')) {
            deleteButton.disabled = true;
            updateButton.disabled = true;
            deleteButton.classList.add('desable');
            updateButton.classList.add('desable');
    
            car.classList.remove('selected');  

        }
    });
       
});

// Delete
deleteButton.addEventListener('click', () => {
    const action = confirm('Подтвердите удаление путевого листа с номером '+ `${selectedCarId}`);
    if (action) {
      $.ajax({
        url: '/ajax/delete2/',
        data: {
          'id': selectedCarId,
        },
        dataType: 'json',
        success: function (data) {
          if (data.deleted) {
            $('.item[data-id=' + selectedCarId + ']').remove();
            selectedCarId = null;
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
    url: `update/${selectedCarId}/`,
    data: {
      'id': selectedCarId,
      'csrfmiddlewaretoken': csrf_token,
    },
    dataType: 'html',
    type: 'POST',
    success: function() { // Добавляем функцию success для обработки ответа
      window.location.href = `update/${selectedCarId}/`;

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