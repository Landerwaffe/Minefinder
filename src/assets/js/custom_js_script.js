
var alertPlaceholder = document.getElementById('liveAlertPlaceholder')
var alertTrigger = document.getElementById('liveAlertBtn')

function alert(message) {
  var wrapper = document.createElement('div')
  wrapper.innerHTML = '<div class="container alert alert-dismissible sub-task" role="alert">' + 
                        '<div class="row">' +
                            '<input class="col-1 input-group-prepend checkBox" value="1" type="checkbox"/>' +
                          
                            '<p class="strikethrough single-line" contentEditable="true">' + message + '</p>' +
                          '</div>' +
                        
                        '<button type="button" class="close" data-dismiss="alert" aria-label="Close"> <span aria-hidden="true">&times;</span> </button>' +  
                      '</div>'
            
  alertPlaceholder.append(wrapper)
}

if (alertTrigger) {
  alertTrigger.addEventListener('click', function () {
    alert('New subtask description here... ')
  })
}

$(document).ready(function () {
  $("#input-res-1").fileinput({
    showUpload: false,
    showClose: false,
    theme: "fas",
    enableResumableUpload: true,
    uploadUrl: "/",
    browseClass: "btn btn-warning",
    layoutTemplates: {
      main1:
        "{preview}\n" +
        "<div class='input-group {class}' '>\n" +
        "   <div class='input-group-btn input-group-prepend'>\n" +
        "       {browse}\n" +
        "       {upload}\n" +
        "       {remove}\n" +
        "   </div>\n" +
        "   {caption}\n" +
        "</div>",
    },
  });
});

function makeComment() {
  var comment = $("[type = text]").val();
  var commentHtml = '<li class="media">' +
                      '<img class="mr-3 rounded-circle" alt="Commenter Profile Preview" src="https://i.imgur.com/nAcoHRf.jpg" />' +
                      '<div class="media-body">' +
                          '<p class="mt-0 mb-1 commenterName">John Smith' +
                              '<small>' +
                                  ' 20th December, 2021' +
                              '</small></p>' +
                          '<p class="bg-comment">' + comment + '</p> ' +
                      '</div>';
		$(commentHtml).appendTo("#comment-section");
    $('#textInput').val('');
}