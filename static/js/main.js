// $(document).ready(function(){
//   // Add smooth scrolling to all links
//   $("a").on('click', function(event) {

//     // Make sure this.hash has a value before overriding default behavior
//     if (this.hash !== "") {
//       // Prevent default anchor click behavior
//       event.preventDefault();

//       // Store hash
//       var hash = this.hash;

//       // Using jQuery's animate() method to add smooth page scroll
//       // The optional number (800) specifies the number of milliseconds it takes to scroll to the specified area
//       $('html, body').animate({
//         scrollTop: $(hash).offset().top
//       }, 800, function(){
   
//         // Add hash (#) to URL when done scrolling (default click behavior)
//         window.location.hash = hash;
//       });
//     } // End if
//   });
// });

// new fullpage("#fullpage", {
//   autoscrolling: true,
//   navigation: true,
//   onLeave:(origin, destination, direction) =>{
//     const section = destination.item;
//     const title = section.querySelector('h1');
//     const tl =new TimelineMax({delay: 0.5});
//     tl.fromTo(title, 0.5, { y: "50", opacity: 0 }, { y: 0, opacity: 1 });
    
//     if(destination.index === 1){
//       const box = document.querySelector('box');
      
//       tl.fromTo(box, 0.5, { y: "50", opacity: 0 }, { y: 0, opacity: 1 });
//     }
//   }
// })