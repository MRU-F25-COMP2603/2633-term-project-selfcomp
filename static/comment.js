document.getElementById("comment-form").addEventListener("submit", async function(event) {
  event.preventDefault();

  const author = document.getElementById("name-input").value.trim();
  const code = document.getElementById("code-input").value.trim();
  const comment = document.getElementById("comment-input").value.trim();

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
