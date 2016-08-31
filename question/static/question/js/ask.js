// Enables tokenized tags
$('#question_tags').tokenfield();

// Submits answer to database without changing page


// $(document).on('submit', '#new_question_form', function(e) {
//  var $input = $('#question_text:input')
//  console.log($input)
//  return false
// })

$('#submit_question_but').click(function(e) {
    var $title = $('#question_title').val();
    var $text = $('#question_text').val();
    var $tags = $('#question_tags').val();
    console.log('hello');
    $.ajax({
     method: 'POST',
     url: '../api/question/',
     data : {
         user: userId,
         title: $title,
         text: $text,
         'csrfmiddlewaretoken': document.cookie.match(/csrftoken=(\w*)/)[1],
     },
     error: function(e) {
         console.log(e);
     },
     dataType: 'json'
 });
    // for (var tag in $tags) {
    //     $.ajax({
    //      method: 'POST',
    //      url: '../api/question/',
    //      data : {
    //          user: userId,
    //          title: $title,
    //          text: $text,
    //          tag: $text,
    //          'csrfmiddlewaretoken': document.cookie.match(/csrftoken=(\w*)/)[1],
    //      },
    //      error: function(e) {
    //          console.log(e);
    //      },
    //      dataType: 'json'
    //  });
    // }
 console.log('hey');
});
