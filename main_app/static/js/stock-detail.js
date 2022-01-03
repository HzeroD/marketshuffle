const dateInput = document.getElementById('id_date')
// const fileInput = document.getElementById('file-input')
// const fileName = document.getElementById('file-name')


//jQuery('#datetimepicker').datetimepicker();

dateInput.addEventListener("click", (evt) => {
    jQuery('#id_date').datetimepicker();
  })

//const picker = jQuery('#datetimepicker').datetimepicker();

// dateInput.addEventListener("click", (evt) => {
//     picker.open()
//   })
  
//   fileInput.addEventListener('change', evt => {
//     const fileToUpload = evt.target.files[0].name
//     if(fileToUpload) {
//       fileName.innerText = fileToUpload
//     } else {
//       fileName.innerText = ""
//     }
//   })

