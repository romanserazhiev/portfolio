$(function() {
  newNewsletterSignUp();
  // preventing from scrolling up when clicking on the Submit button
  $('.k15t-subscribe-button').on('click', function(e) {
    e.preventDefault();
  })
});

function newNewsletterSignUp () {
  const newsletterBanner = $('.animated-newsletter-sign-up-full');

  if (!newsletterBanner.length || !newsletterBanner.is(':visible')) {
    return false;
  }

  const newsletterBannerWrapper = $('.animated-newsletter-sign-up', newsletterBanner);
  let oldBannerOpacity = 1;

  $(document).on('scroll', newsletterBanner, onNewsletterBannerScroll)
  
  function onNewsletterBannerScroll() {
    const scrollBarPosition = $(document).scrollTop();
    const windowHeight = $(window).height();
    const bannerOffset = newsletterBanner.offset().top;
    const bannerTopPosition = bannerOffset - windowHeight;
    const bannerHeight = newsletterBanner.height();
    let bannerBottomPosition = bannerHeight + bannerTopPosition;
    let bannerOpacity = 1;
    let p;
    
    function updateStyles(bannerOp) {
      const opacity = Math.abs(bannerOp - 1);
      const startScale = 0.9;
      
      p = (100 - 100 * bannerOp) / 100;
      let scale = (1 - startScale) * p + startScale;
    
      if (scale > 1) {
        scale = 1;
      }
    
      newsletterBannerWrapper.css({
        opacity: opacity,
        '-webkit-transform': 'scale(' + scale + ')',
        transform: 'scale(' + scale + ')',
      });
    }

    if (bannerHeight > windowHeight) {
      bannerBottomPosition = (bannerTopPosition + windowHeight) - (windowHeight / 4);
    }

    if (scrollBarPosition > bannerTopPosition) {
      p = (scrollBarPosition - bannerTopPosition) * 100 / (bannerBottomPosition - bannerTopPosition);
      bannerOpacity = (100 - p) / 100;

      if (bannerOpacity < 0) {
        bannerOpacity = 0;
      }
    }

    if (bannerOpacity !== oldBannerOpacity) {
      oldBannerOpacity = bannerOpacity;
      updateStyles(bannerOpacity);
    }
  }
}