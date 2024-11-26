
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
