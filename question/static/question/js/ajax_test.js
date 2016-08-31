function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});


// Posts answer to database
function postAnswer(userInput, userData, questionPk) {
  $.ajax({
    type: 'post',
    url: '../api/answer/',
    data: {
      user: userData.id,
      question: questionPk,
      text: userInput
    },
    success: function(data) {
      writeAnswersToPage(data, userData)
    },
    error: function(e) {
      console.log(e);
    },
    dataType: 'json'
  })
}


function writeAnswersToPage(data, userData) {
  var timestamp = new Date().toLocaleString()
  $('.answers').append(
    '<p>' + data.text + '</p><br /><p>Said by ' + userData.username + ' on ' + timestamp + '</p>')
}
  $('#answerField').empty()

var questionPk = $('.question').attr('id')


// Submits answer to database without changing page
$(document).on('submit', '#answerForm', function(e) {
  var $input = $('#answerField:input')
  postAnswer($input.val(), userData, questionPk)
  e.preventDefault();
})
