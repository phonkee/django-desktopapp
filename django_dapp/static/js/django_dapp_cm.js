(function ($) {
  $(document).ready(function () {
    $('textarea').each(function () {
      var editor = CodeMirror.fromTextArea($(this)[0], {
        mode: 'markdown',
        lineNumbers: true,
        theme: "default",
        extraKeys: {"Enter": "newlineAndIndentContinueMarkdownList"},
        highlightFormatting: true,
      });
    })
  })
})
(django.jQuery);
