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


// Grabs answers from the api based on question id
function getAnswers(questionPk) {
  $.get({
    url: '../api/question/' + questionPk,
    success: function(data) {
      $.each(data.answer_set, function(key, value) {
        getUsernameAndWriteToPage(value)
      })
    }
  })
}

// Grabs the username from the user api for the answer
function getUsernameAndWriteToPage(value) {
  var userPk = value.user.toString()
  var username;
  $.get({
    url: '../api/username/' + userPk,
    success: function(data) {
      var username = data.username;
      writeAnswersToPage(value, username)
    }
  })
  return username
}

// Appends answers to page
function writeAnswersToPage(value, username) {
  $('.answers').append(
    '<p>' +value.text + '</p><br /><p>Said by ' + username + ' on ' + value.timestamp + '</p>')
}


// Posts answer to database
function postAnswer(userInput, userData, questionPk) {
  $.ajax({
    type: 'post',
    url: '../api/answer/',
    data: {
      user: userData,
      question: questionPk,
      text: userInput
    },
    error: function(e) {
      console.log(e);
    },
    dataType: 'json'
  })
}


var questionPk = $('.question').attr('id')
getAnswers(questionPk)

// Submits answer to database without changing page
$(document).on('submit', '#answerForm', function(e) {
  var $input = $('#answerField:input')
  postAnswer($input.val(), userData, questionPk)
  $('.answers').empty()
  getAnswers(questionPk)
  e.preventDefault();
})
