/**
 * @name NoReplyMention
 * @description Automatically sets replies to not mention target
 * @author somebody
 * @authorId 153146360705712128
 * @authorLink https://github.com/somebody1234
 * @version 0.0.2
 * @source https://raw.githubusercontent.com/somebody1234/userscripts/master/NRM.plugin.js
 * @updateUrl https://raw.githubusercontent.com/somebody1234/userscripts/master/NRM.plugin.js
 */
module.exports = class NoReplyMention {
  constructor() {
    const {Webpack, Webpack: {Filters}} = BdApi;

    [this.i18n, this.classes] = Webpack.getBulk(
      {filter: m => m.getLocale && m.Messages?.REPLY_MENTION_ON},
      {filter: Filters.byProps("mentionButton")}
    );
  }

  setShiftDown = function(event){
    if(event.keyCode === 16 || event.charCode === 16){
      var instance = BdApi.Plugins.get("NoReplyMention").instance;

      instance.shiftDown = true;
      instance.controller.abort();
    }
  }

  setShiftUp = function(event){
      if(event.keyCode === 16 || event.charCode === 16){
        var instance = BdApi.Plugins.get("NoReplyMention").instance;

        instance.shiftDown = false;
        instance.controller = new AbortController()
        document.addEventListener('keydown', instance.setShiftDown, {passive: false, signal: instance.controller.signal});
    }
  }


  start() {
    this.shiftDown = false;
    this.controller = new AbortController();
    document.addEventListener('keydown', this.setShiftDown, {passive: false, signal: this.controller.signal});
    document.addEventListener('keyup', this.setShiftUp, {passive: false});
  }

  stop() {
    document.removeEventListener('keydown', this.setShiftDown);
    document.removeEventListener('keyup', this.setShiftUp);
  }
  
  observer({addedNodes}) {

    if (!this.i18n || !this.classes) return;
    
    for (const node of addedNodes) {
      if (node.nodeType === Node.TEXT_NODE) continue;

      const elements = node.getElementsByClassName(this.classes.mentionButton);

      if (!elements.length) continue;
      
      for (const element of elements) {
        if (element.textContent === this.i18n.Messages.REPLY_MENTION_ON || this.shiftDown) {
          element.click();
        }
      }
    }  
  }
}
