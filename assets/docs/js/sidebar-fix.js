document.addEventListener('DOMContentLoaded', function() {
  function adjustSidebar() {
    const sidebar = document.querySelector('.sidebar-content');
    if (sidebar) {
      const headerHeight = document.querySelector('.top-header') ? 
        document.querySelector('.top-header').offsetHeight : 72;
      const availableHeight = window.innerHeight - headerHeight - 20; // 20px de margen
      
      sidebar.style.maxHeight = availableHeight + 'px';
      sidebar.style.height = 'auto';
      sidebar.style.overflowY = 'auto';
    }
  }
  
  adjustSidebar();
  window.addEventListener('resize', adjustSidebar);
  
  document.querySelectorAll('.sidebar-dropdown button').forEach(button => {
    button.addEventListener('click', function() {
      setTimeout(adjustSidebar, 300);
    });
  });
});