var $voteUp = $("#question_vote_up");
var $voteDown = $("#question_vote_down");
var $voteCount = $("#question_vote_counter");

$voteUp.click(function(e){
    var newVal = $("#question_vote_counter").val() + 1;
    $("#question_vote_counter").empty().append(newVal);
    // Add ajax to make this legitimate
});


$voteDown.click(function(e){
    // $voteCount.empty().append(1);
    // Add ajax to make this legitimate
    var newVal = $voteCount.val() - 1;
    $voteCount.empty().append(newVal);
});


// $('#submit_question_but').click(function(e) {
//     $.ajax({
//      method: 'PATCH',
//      url: '../api/question/',
//      data : {
//          vote: userId,
//          'csrfmiddlewaretoken': document.cookie.match(/csrftoken=(\w*)/)[1],
//      },
//      error: function(e) {
//          console.log(e);
//      },
//      dataType: 'json'
//  });
