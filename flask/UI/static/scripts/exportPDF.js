document.addEventListener("DOMContentLoaded", () => {
    // Escuchamos el click del botón
    
    const $boton = document.querySelector("#btnCrearPdf");
    $boton.addEventListener("click", () => {
     
        let eleToConvert = document.getElementById('output_main'); // <-- Aquí puedes elegir cualquier elemento del DOM

        var opt = {
            margin:       [1, 2],
            filename:     'Resultado_analisis.pdf',
            image:        { type: 'jpeg', quality: 1 },
            html2canvas:  { scale: 10,
                            with:900,
                            height:750,
                            y: 6,  scrollY: 10},
            jsPDF:        { unit: 'mm', format: 'a4', orientation: 'l' }
          };
          html2pdf().set(opt).from(eleToConvert).save();
            
        
            
    });
});