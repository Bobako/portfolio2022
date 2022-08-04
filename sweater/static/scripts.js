$(document).ready(function () {
    let height = (-$(".task").outerHeight() + 2) + "px";
    $("main").css("--task-height", height);
    console.log(height);
});

function toggleTask() {
    $(".task").toggleClass("active");
    $(".toggle-task").toggleClass("pressed");

}