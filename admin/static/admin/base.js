$("body section header").mousedown(function(event) {
  var i = $(this);
  i
    .data('is_mouse_down', true)
    .data('prev_mouse_x', event.pageX)
    .data('prev_mouse_y', event.pageY);
  $("body section").css("z-index", 0);
  i.parent().css("z-index", 1);
  $("body").data('windows_moving', i);
});

$("body section header").mouseup(function() {
  $(this)
    .data('is_mouse_down', false)
    .removeData('prev_mouse_x')
    .removeData('prev_mouse_y');
  $("body").data('windows_moving', null);
});

$("body section header").mousemove(function(event) {
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

$("body section header").mouseout(function(event) {
  $(this).data('is_mouse_lost', true);
});

$("body section header").mouseover(function(event) {
  $(this).data('is_mouse_lost', false);
});

$("body section").mousedown(function(event) {
  $("body section").css("z-index", 0);
  $(this).css("z-index", 1);
});

$("body section header").each(function(i) {
  $(this).parent()
    .css("opacity", 0)
    .animate({
      top: String(i*2+3) + "em",
      left: String(i*5+4) + "em",
      opacity: 1,
    }, 1500);
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

$("body aside .ventanas_activas").each(function(i) {
  var t = $(this);
  t.empty();
  $("body section header").each(function(j) {
    t.append("<div>"+$(this).html()+"</div>");
  });
  var ventanas = $("body section");
  t.children().each(function(j) {
    $(this)
      .css("opacity", 0)
      .animate({
        opacity: 1,
      }, 2000);
    $(this).click(function() {
      var v = $(ventanas[j]);
      if (parseInt(v.css("z-index")) == 1) {
        v.animate({
          opacity: 0,
        }, 500);
        window.setTimeout(function() {
          v
            .css("visibility", "hidden")
            .css("z-index", 0);
        }, 1000);
      } else {
        v
          .css("visibility", "visible")
          .animate({
            opacity: 1,
          }, 1000)
          .mousedown();
      }
    });
  });
});



