from aiogram import executorfrom my_bots.bot2.config import dpfrom handlers import client, callback, extra, adminimport loggingadmin.register_handlers_admin(dp)client.register_handlers_client(dp)callback.register_handlers_callback(dp)#должно всегда последнимextra.register_handlers_extra(dp)'''запускаются все остальные файлы    если запустить этот файл'''if __name__ == '__main__':    logging.basicConfig(level=logging.INFO)    executor.start_polling(dp, skip_updates=True)