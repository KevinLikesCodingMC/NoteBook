$(function() {
    var EditormdView;
    editormd.katexURL = {
        js  : "/resource/katex/katex.min",
        css : "/resource/katex/katex.min",
    };
    EditormdView = editormd.markdownToHTML("editor-html-view", {
        htmlDecode      : "style,script,iframe",
        taskList        : true,
        tex             : true,
    });
});