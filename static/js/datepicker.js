
    $(function () {
        $('#id_date').datepicker({
            inline: true,
            sideBySide: true,
            todayBtn: false,

            format: 'DD.MM.YYYY', /*remove this line if you want to use time as well */
            minDate: getFormattedDate(new Date())
        });
     function getFormattedDate(date) {
            var day = date.getDate();
            var month = date.getMonth() + 1;
            var year = date.getFullYear().toString().slice(2);
            return day + '-' + month + '-' + year;
        }
        
       
      
    });
    