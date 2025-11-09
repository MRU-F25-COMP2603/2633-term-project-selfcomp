/*This handles our dropdowns in the course-list section*/
const groups = document.querySelectorAll('.group');

groups.forEach(group => {
  const title = group.querySelector('.group-title');
  const list = group.querySelector('.course-list');

  title.addEventListener('click', () => {
    // Toggle active state
    group.classList.toggle('active');

    // Expand or collapse smoothly
    if (group.classList.contains('active')) {
      list.style.maxHeight = list.scrollHeight + "px";
    } else {
      list.style.maxHeight = null;
    }
  });
});