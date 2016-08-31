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
  $('#answerField').reset()

var questionPk = $('.question').attr('id')

// Submits answer to database without changing page
$(document).on('submit', '#answerForm', function(e) {
  var $input = $('#answerField:input')
  postAnswer($input.val(), userData, questionPk)
  return false
})


$(document).on('submit', '#new_question_form', function(e) {
  var $input = $('#question_text:input')
  console.log($input)
  return false
})
