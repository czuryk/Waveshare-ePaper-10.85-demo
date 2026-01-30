# Waveshare-ePaper-10.85-demo
Waveshare ePaper 10.85 demo

This is a project for my dashboard, which features a display [Waveshare 10.85''](https://www.waveshare.com/wiki/10.85inch_e-Paper_HAT+), currently one of the largest available.

The screen consists of two matrices combined into a single display, with one controller and a single interface (HAT) for connecting to a Raspberry Pi. From a user’s perspective, you work with this as a single display - the driver handles the rest.

In my implementation, I use a Raspberry Pi Zero 2W. The large display allows you to show a lot of useful information at once, while the Pi Zero 2W serves as an easily programmable heart of the dashboard.

One of the main advantages of this display, and the reason it’s ideal for a dashboard - even though it’s only black and white - is its support for partial refresh. This allows you to update specific elements on the screen without having to redraw the entire display. Please note that most color displays do not support partial updates and cannot be used as dashboards requiring frequent screen refreshes.

This sample code also includes a patched library that resolves an issue with the Waveshare library's partial refresh feature. Both displays now operate correctly in partial refresh mode as a single unit.

<img width="1200" height="896" alt="cover1" src="https://github.com/user-attachments/assets/aa613610-1c12-4f89-b783-3dcc70e41608" />
<img width="1200" height="896" alt="cover2" src="https://github.com/user-attachments/assets/e87866a5-9507-4a80-bc16-856949eca8f6" />
