$(function() {
    editormd.katexURL = {
        js  : "/resource/katex/katex.min",
        css : "/resource/katex/katex.min",
    };
    var editor = editormd("editor", {
        width  : "100%",
        height : "500px",
        path   : "/resource/editormd/lib/",
        saveHTMLToTextarea : true,
        tex  : true,
        toolbarIcons : function() {
            return [
                "undo", "redo", "|",
                "bold", "del", "italic", "quote", "ucwords", "uppercase", "lowercase", "|",
                "h1", "h2", "h3", "h4", "h5", "h6", "|",
                "list-ul", "list-ol", "hr", "|",
                "link", "reference-link", "image", "code", "preformatted-text", "code-block", "table", "datetime", "html-entities", "pagebreak", "|",
                "goto-line", "watch", "preview", "fullscreen", "clear", "search", "|",
                "help", "info",
            ]
        },
        imageUpload    : true,
        imageFormats   : ["jpg", "jpeg", "gif", "png", "bmp", "webp"],
        imageUploadURL : "/upload/image/",
    });
});