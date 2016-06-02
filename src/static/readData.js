var navSettings,
    navigatorApi = {

        settings: {
            navig: window.navigator,
            battCharging: "#batteryCharging",
            hardware: "#hardware"
        },

        init: function () {
            navSettings = navigatorApi.settings;
            navigatorApi.battery();
            navigatorApi.hardware();
        },

        battery: function () {
            navSettings.navig.getBattery().then(function (batt) {
                navigatorApi.batterText({
                    level: batt.level,
                    charging: batt.charging
                });
            })
        },

        batterText: function (battInfo) {
            var text = "Your battery is " + battInfo.level * 100.0 + "% charged, ";
            if (battInfo.charging) {
                text = text + "and is plugged in";
            } else {
                text = text + "but is not plugged in";
            }
            htmlUpdate.addText(text, navSettings.battCharging);
        },

        hardware: function () {
            var text = "You have " + navSettings.navig.hardwareConcurrency + " logical cores available";
            htmlUpdate.addText(text, navSettings.hardware);
        }



    };

var windowSettings,
    windowApi = {
        settings: {
            screenId: "#screen",
            historyId: "#history"
        },
        init: function () {
            windowSettings = windowApi.settings;
            windowApi.screenSize();
            windowApi.historyLength();
        },
        screenSize: function () {
            var h = window.screen.availHeight;
            var w = window.screen.availWidth;
            text = "Your screen is " + w + "px wide and " + h + "px tall";
            htmlUpdate.addText(text, windowSettings.screenId);
        },

        historyLength: function () {
            var hLen = window.history.length;
            text = "You have been to " + hLen + " pages in this tab";
            htmlUpdate.addText(text, windowSettings.historyId);
        }
    };


var htmlUpdate = {

    addText: function (text, id) {
        document.querySelector(id).textContent = text;
    }
};


(function () {
    navigatorApi.init();
    windowApi.init();
})();