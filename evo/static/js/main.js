$(document).ready(function(){
      var scroll_start = 0;
      var startchange = $('.navbar');
      var offset = startchange.offset();
      $(document).scroll(function() {
          scroll_start = $(this).scrollTop();
          if(scroll_start > offset.top+100) {
              $('.navbar').css('background-color', 'rgba(0,0,0,0.8)');
          } else {
              $('.navbar').css('background-color', 'transparent');
          }
      });
      if(($(window).height()) > 750){
           $('section').height($(window).height());
      $(window).resize(function(){
          $('section').height($(window).height());
      });
      }
  });