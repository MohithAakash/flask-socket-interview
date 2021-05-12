$(document).ready(function () {

    var socket = io.connect('http://' + document.domain + ':' + location.port);

    // socket.on('connect', function () {
    //     // socket.emit('my event', {
    //     //     data: 'User Connected'
    //     // });
    // });

    var form = $('form').on('submit', function (e) {
        e.preventDefault()
        let interviewer = $('input.interviewer-name').val()
        let score1 = $('input.parameter1').val()
        let score2 = $('input.parameter2').val()
        let score3 = $('input.parameter3').val()
        let score4 = $('input.parameter4').val()

        socket.emit('my event', {
            interviewer: interviewer,
            parameter1: score1,
            parameter2: score2,
            parameter3: score3,
            parameter4: score4
        });

        $(".form").hide("fast");
        $(".form").remove();
        $(".message-holder").append(
            "<h3>Please wait for the other interviewers to submit their scores</h3><div class='loader' style='display: inline-block;'></div>"
        );
        $(".message-holder").fadeIn();

    });

    socket.on('my response', function (scores) {
        console.log(scores);

        var score;
        var x;
        for (score of scores) {
            var row = "";
            for (x in score) {
                row += "<td>" + score[x] + "</td>";
            }
            tableBody = $("table tbody");
            tableBody.append("<tr>" + row + "</tr>")
        }

        $(".message-holder").hide("fast");
        $(".tbl").show("slow");
    });
});