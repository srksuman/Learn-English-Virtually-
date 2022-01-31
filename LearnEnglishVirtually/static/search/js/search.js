$(document).ready(function(){
     
        $('#search').on('keyup',function(){
            var searchTerm = $(this).val().toLowerCase();
            $('.searchContent').each(function(){
                var blockString = $(this).text().toLowerCase();
                if(blockString.indexOf(searchTerm)===-1){
                    $(this).hide();
                    console.log()
                    
                }else{
                    $(this).show();
                   
                }
            })

        })
        
    });
