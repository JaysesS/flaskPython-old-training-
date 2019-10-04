function getSize() {
    $.ajax({
        type: "POST",
        url: "/getSize",
        data: $('#formLen').serialize(),
        type: 'POST',
        success: function(response) {
            var json = jQuery.parseJSON(response)
            $('#len').html("Длина текста: " + json.len)
            console.log(response);
        },
        error: function(error) {
            console.log(error);
        }
    });
}

function generate() {
    $.ajax({
        type: "POST",
        url: "/generate",
        data: $('#formGenerate').serialize(),
        type: 'POST',
        success: function(response) {
            var json = jQuery.parseJSON(response)
            $('#number').html(json.number)
            console.log(response);
        },
        error: function(error) {
            console.log(error);
        }
    });
}

function checking() {
    $.ajax({
        type: "POST",
        url: "/checking",
        type: 'POST',
        success: function(response) {
            var json = jQuery.parseJSON(response)
            if (json.atMoment != 'nope'){
                var e = $("<p>" + (json.atMoment).trim() + "<p>")
                e.attr('id', 'hash')
                $('#check').append(e)
            }
            console.log(response);
        },
        error: function(error) {
            console.log(error);
        }
    });
}

function viewTime(){
    var x = document.getElementById("time").textContent
    document.getElementById("time").innerHTML = parseInt(x) + 1
}

window.onload = function() {

    let checker = setInterval(() => checking(), 2000);
    setTimeout(() => { clearInterval(checker); console.log('stop'); }, 60000);

    setInterval(viewTime, 1000)

}