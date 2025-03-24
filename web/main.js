// web/main.js
function themeSelected() {
    const theme = document.getElementById('theme-selector').value;
    eel.theme_selected(theme);
}

eel.expose(updateTopBar);
function updateTopBar(color) {
    document.getElementById('top-bar').style.backgroundColor = color;
}