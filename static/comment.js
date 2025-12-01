// comment.js
// Used in our HTML to take user input for runComment in app.py
// Sources
// https://stackoverflow.com/questions/6623231/remove-all-white-spaces-from-text

document.getElementById("comment-form").addEventListener("submit", async function(event) {
  event.preventDefault();

  //trim white space
  const author = document.getElementById("name-input").value.trim();
  const comment = document.getElementById("comment-input").value.trim();

  //trim whitespace and format
  const code = document.getElementById("code-input").value.trim().replaceAll(/\s/g,'').toUpperCase();

  // Send data to backend
  const response = await fetch("/api/addComment", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ code, author, comment })
  });

  const result = await response.json();
  document.getElementById("output").textContent = result.message;

  document.getElementById("comment-form").reset();
});
