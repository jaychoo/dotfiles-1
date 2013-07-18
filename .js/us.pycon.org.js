if (window.location.pathname == '/2014/reviews/section/talks/') {
    $(".span2").append("<br><button id='hideshow' class='btn'>Hide Reviewed Talks</button>");
    $("#hideshow").click(function() {
        if ($(this).text() == "Hide Reviewed Talks") {
            $("tbody tr:not(.no-vote)").hide();
            $(this).text('Show Reviewed Talks');
        } else {
            $("tbody tr:not(.no-vote)").show();
            $(this).text('Hide Reviewed Talks');
        }
    });
}
