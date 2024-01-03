
init -1 python:

    import discord_rpc
    import time

    class DiscordRichPresence:
        """
        Esta clase permite hacer visible al juego en Discord mediante
        Discord Rich Presence (RPC).
        Esto solo funciona en PC, y para que la actividad sea visible, el jugador
        debe tener instalado el cliente de Discord en su PC.

        No se asegura que el juego sea visible si se usa Discord desde un navegador.
        """
        def __init__(self):
            self.client = "1189958905023967363"
            self.is_running = True
            self.runtime_epoch = time.time()

            self.cb_methods = {
                            "ready" : self.rpc_ready,
                            "disconnected" : self.rpc_disconnect,
                            "error" : self.rpc_error}
        
        ## ---------------------------------------------------------------------- ##
        ## Métodos callback para reportar actividad de Discord RPC
        def rpc_ready(self, userdict):
            #logger(logging.info, "Discord RPC running on user \"%(username)s\"..." % userdict)
            #rbs_alert(__("¡Ren'Py RhythmBeats ya es visible en Discord!"), 0, "ui_icon_discord")
            print("Ready. RPC payload:", userdict)

        def rpc_disconnect(self, code, msg):
            #logger(logging.warning, "Discord RPC disconnected.")
            #logger(logging.warning, "Error code: %s" % code)
            #logger(logging.warning, "Details: %s" % msg)

            #rbs_alert(content="(%s) %s" %(code, msg), status=1, icon="ui_icon_warning")
            print("Disconnected: (%s) %s" %(code, msg))

        def rpc_error(self, code, msg):
            #logger(logging.error, "Error in Discord RPC runtime.")
            #logger(logging.warning, "Error code: %s" % code)
            #logger(logging.warning, "Details: %s" % msg)

            #rbs_alert("(%s) %s" %(code, msg), status=1, icon="ui_icon_warning")
            print("Unexpected error: (%s) %s" %(code, msg))

        ## ---------------------------------------------------------------------- ##
        ## Métodos de ejecución y de actividad de Discord RPC
        def set_status(self, state = None, details = "", image_text = "Lack Of Colors"):
            """
            Este método actualiza el estado actual visible en el perfil de
            Discord.
            """
            if self.is_running:
                discord_rpc.update_presence(
                    **{
                        "state" : state,
                        "details" : details,
                        "start_timestamp": self.runtime_epoch,
                        "large_image_key": "ai-icon",
                        "large_image_text" : image_text
                    }
                )

        def stop(self):
            """
            Este método detiene toda actividad de RPC (recomendado por la
            documentación de Discord.

            Llama a este método en el label especial `quit`.
            """

            if self.is_running:
                #logger(logging.info, "Discord RPC service stopped.")
                #rbs_alert(__("Discord RPC deshabilitado."), icon="ui_icon_discord")
                self.is_running = False

        def rpc_updater(self):
            """
            Este método ejecuta la transmisión del status en el perfil de Discord.
            Actualiza el status cada 3 segundos en la medida de lo posible.
            """

            discord_rpc.initialize(self.client, callbacks=self.cb_methods, log=False)

            while True:
                try:
                    discord_rpc.update_connection()
                    discord_rpc.run_callbacks()

                except Exception as rpc_upd_error:
                    #logger(logging.info, "Discord thread error: %s" % repr(rpc_upd_error))
                    print("Thread error:", rpc_upd_err)
                finally:
                    if self.is_running:
                        time.sleep(3)
                    else:
                        discord_rpc.shutdown()
                        break

        def rpc_start(self):
            """
            Este método ejecuta el hilo de Discord RPC en paralelo al hilo principal
            del juego.
            """
            #logger(logging.info, "Starting Discord RPC service...")
            #rbs_alert(__("Ren'Py RhythmBeats se está conectando con Discord..."), icon="ui_icon_discord")
            renpy.invoke_in_thread(fn=self.rpc_updater)

    rpc = DiscordRichPresence()