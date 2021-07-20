MyBanners = new Array('UI/static/images/enviar.png', '/home/jules/Documentos/Personal/Sentiment_analyzer/UI/static/images/i_pdf.png')
banner = 0
function ShowBanners() {
    if (document.images) {
        banner++
        if (banner == MyBanners.length) {
            banner = 0
        }
        document.ChangeBanner.src = MyBanners[banner]
        setTimeout("ShowBanners()", 5000)
    }
}