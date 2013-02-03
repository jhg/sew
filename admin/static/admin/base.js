$("section header").mousedown(function(event) {
  var i = $(this);
  i
    .data('is_mouse_down', true)
    .data('prev_mouse_x', event.pageX)
    .data('prev_mouse_y', event.pageY);
  $("section").css("z-index", 0);
  i.parent().css("z-index", 1);
  $("body").data('windows_moving', i);
});

$("section header").mouseup(function() {
  $(this)
    .data('is_mouse_down', false)
    .removeData('prev_mouse_x')
    .removeData('prev_mouse_y');
  $("body").data('windows_moving', null);
});

$("section header").mousemove(function(event) {
  var i = $(this);
  if (i.data('is_mouse_down')) {
    var new_x = event.pageX - i.data('prev_mouse_x');
    var new_y = event.pageY - i.data('prev_mouse_y');
    i.parent()
      .css("left", $(this).parent().position().left + new_x)
      .css("top", $(this).parent().position().top + new_y);
    i
      .data('prev_mouse_x', event.pageX)
      .data('prev_mouse_y', event.pageY);
  }
});

$("section header").mouseout(function(event) {
  $(this).data('is_mouse_lost', true);
});

$("section header").mouseover(function(event) {
  $(this).data('is_mouse_lost', false);
});

$("section").mousedown(function(event) {
  $("section").css("z-index", 0);
  $(this).css("z-index", 1);
});

$("section header").each(function(i) {
  $(this).parent()
    .css("top", String(i*3+3.75) + "em")
    .css("left", String(i*2.5+1.25) + "em");
});

$("body").data('windows_moving', null);
$(document).mousemove(function(event) {
  var i = $("body").data('windows_moving');
  if (i != null) {
    if (i.data('is_mouse_lost')) {
      var new_x = event.pageX - i.data('prev_mouse_x');
      var new_y = event.pageY - i.data('prev_mouse_y');
      i.parent()
        .css("left", i.parent().position().left + new_x)
        .css("top", i.parent().position().top + new_y);
      i
        .data('prev_mouse_x', event.pageX)
        .data('prev_mouse_y', event.pageY);
    }
  }
});



