document.addEventListener("DOMContentLoaded", () => {
    const themeToggle = document.getElementById("themeToggle");
    const currentTheme = localStorage.getItem("theme");

    if (currentTheme === "dark") {
        document.body.classList.add("dark-mode");
    }

    themeToggle.addEventListener("click", () => {
        document.body.classList.toggle("dark-mode");
        const theme = document.body.classList.contains("dark-mode") ? "dark" : "light";
        localStorage.setItem("theme", theme);
        const themeIcon = document.getElementById("themeIcon");
        themeIcon.textContent = theme === "dark" ? "🌙" : "🌞";
    });
});

function openEditPopup(id, title, content) {
    console.log("openEditPopup");
    document.getElementById('journalId').value = id;
    document.getElementById('editTitle').value = title;
    document.getElementById('editContent').value = content;
    document.getElementById('editPopup').style.display = 'block';
}
    
function closeEditPopup() {
    console.log("closeEditPopup");
    document.getElementById('editPopup').style.display = 'none';
}
