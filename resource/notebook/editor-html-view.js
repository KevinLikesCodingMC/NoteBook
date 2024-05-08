$(function() {
    var EditormdView;
    EditormdView = editormd.markdownToHTML("editor-html-view", {
        htmlDecode      : "style,script,iframe",
        taskList        : true,
        tex             : true,
    });
});