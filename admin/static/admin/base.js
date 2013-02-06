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
  $("body").removeData('windows_moving');
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

$("body section").each(function(i) {
  $(this)
    .css("opacity", 0)
    .animate({
      top: String(i*2+3) + "em",
      left: String(i*5+4) + "em",
      opacity: 1,
    }, 1500);
});

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

$("body section canvas").each(function(i) {
  var t = $(this);
  t.data("context", this.getContext('2d'));
  t.data("mouse_down", false);
  $(this)[0].width = 2 * parseInt($(this).css("width"));
  $(this)[0].height = 2 * parseInt($(this).css("height"));
  t.dblclick(function() {
    $(this)[0].width = 2 * parseInt($(this).css("width"));
    $(this)[0].height = 2 * parseInt($(this).css("height"));
  });
  t.mousedown(function(event) {
    var rx = parseInt($(this).parent().css("left"));
    var ry = parseInt($(this).parent().css("top")) + parseInt($(this).parent().css("padding-top"));
    var cw = $(this)[0].width / parseInt($(this).css("width"));
    var ch = $(this)[0].height / parseInt($(this).css("height"));
    $(this).data("mouse_down", true);
    $(this).data("rx", rx);
    $(this).data("ry", ry);
    $(this).data("cw", cw);
    $(this).data("ch", ch);
    var c = $(this).data("context");
    c.beginPath();
    c.moveTo((event.clientX - rx) * cw, (event.clientY - ry) * ch);
  });
  t.mousemove(function(event) {
    if (t.data("mouse_down")) {
      var rx = $(this).data("rx");
      var ry = $(this).data("ry");
      var cw = $(this).data("cw");
      var ch = $(this).data("ch");
      var c = $(this).data("context");
      c.strokeStyle = "#" + String(event.clientX % 10) + String((event.clientX + event.clientY) % 10) + String(event.clientY % 10);
      c.lineTo((event.clientX - rx) * cw, (event.clientY - ry) * ch);
      c.lineWidth = 6;
      c.stroke();
      c.closePath;
      c.beginPath();
      c.moveTo((event.clientX - rx) * cw, (event.clientY - ry) * ch);
    }
  });
  t.mouseup(function(event) {
    var c = $(this).data("context");
    c.closePath;
    $(this).data("mouse_down", false);
  });
});


