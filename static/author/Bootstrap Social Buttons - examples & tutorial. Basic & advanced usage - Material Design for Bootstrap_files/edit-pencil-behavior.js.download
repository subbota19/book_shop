'use strict';

jQuery(function ($) {

  $('.edit-page-pencil').hover(
    function (e) {

      var $this = $(this);

      $this.css("opacity", 1);
      replaceClass($this.find('.edit-page-pencil-icon'), 'grey-text', 'green-text');
      replaceClass($this.find('.edit-page-pencil-text'), 'grey-text', 'blue-text');
    },
    function (e) {

      var $this = $(this);

      $this.css("opacity", 0.3);
      replaceClass($this.find('.edit-page-pencil-icon'), 'green-text', 'grey-text');
      replaceClass($this.find('.edit-page-pencil-text'), 'blue-text', 'grey-text');
    }
  );

  function replaceClass($element, replacementClass, replacerClass) {

    $element.removeClass(replacementClass).addClass(replacerClass);
  }
});
