$(document).on('submit', '#answerForm', function(e) {
  // $.ajax({
  //   url: '/',
  //   type: 'post',
  //   data: {
  //
  //   }
  // })
  console.log($('#answerField').value)
  e.preventDefault();
})
// Now we have the question id for attaching to form
// TODO get user, text
