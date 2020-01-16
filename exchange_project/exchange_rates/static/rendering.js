$('#submit_button').click(function(){
    event.preventDefault();
    console.log('form submited')
    send_data();
});

function send_data(){
    console.log("send data is working")
    $.ajax({
        url : "calculations",
        type : "GET",
        data : {
            money : $('#money').val(),
            from_currency: $('#from_currency').val(),
            to_currency: $('#to_currency').val()
        },

        success : function(response_data) {
            $('#result').html("<b>Result:" + response_data.result_of_convert + "</b>")
            console.log(response_data);
            console.log("success");
        },

        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! Occurred error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>");
            console.log(xhr.status + ": " + xhr.responseText);
        }
    });
};
