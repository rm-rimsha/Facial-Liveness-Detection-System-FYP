const imageUpload = document.getElementById('imageUpload');

Promise.all([
    faceapi.nets.faceLandmark68Net.loadFromUri('./models'),
    faceapi.nets.ssdMobilenetv1.loadFromUri('./models'),
    faceapi.nets.faceRecognitionNet.loadFromUri('./models'),
    faceapi.nets.tinyFaceDetector.loadFromUri('./models')
]).then(start)

function start() {
    const container = document.createElement('div');
    container.style.position = 'relative';
    document.body.append(container);
    document.body.append('Loaded');

    const zip = new JSZip();

    imageUpload.addEventListener('change', async () => {
        if (imageUpload.files.length > 0) {
            const fileArray = Array.from(imageUpload.files);
            for (let i = 0; i < fileArray.length; i++) {
                const file = fileArray[i];
                const image = await faceapi.bufferToImage(file);
                container.append(image);
                const canvas = faceapi.createCanvasFromMedia(image);
                container.append(canvas);
                const displaySize = { width: image.width, height: image.height };
                faceapi.matchDimensions(canvas, displaySize);
                const detections = await faceapi.detectAllFaces(image).withFaceLandmarks().withFaceDescriptors();
                const resizedDetections = faceapi.resizeResults(detections, displaySize);
                canvas.style.position = 'absolute';
                canvas.style.top = 0;
                canvas.style.left = 0;
                canvas.width = displaySize.width;
                canvas.height = displaySize.height;
                resizedDetections.forEach(async (detection) => {
                    const box = detection.detection.box;
                    const drawBox = new faceapi.draw.DrawBox(box);
                    drawBox.draw(canvas);
                    const faceCanvas = document.createElement('canvas');
                    faceCanvas.width = 112;
                    faceCanvas.height = 112;
                    const faceCtx = faceCanvas.getContext('2d');
                    faceCtx.drawImage(
                        image,
                        box.x,
                        box.y,
                        box.width,
                        box.height,
                        0,
                        0,
                        112,
                        112
                    );
                    const imageURL = faceCanvas.toDataURL();
                    const fileName = `${file.name.split('.').slice(0, -1).join('.')}.jpg`;
                    const link = document.createElement('a');
                    link.href = imageURL;
                    link.setAttribute('download', fileName);
                    link.innerHTML = 'Download';
                    container.append(link);
                    // add the image file to the zip folder
                    zip.file(fileName, imageURL.split(',')[1], { base64: true });
                });
            }
            // generate the zip folder and download it
            zip.generateAsync({ type: 'blob' }).then(function (content) {
                const zipLink = document.createElement('a');
                zipLink.href = URL.createObjectURL(content);
                zipLink.download = 'face_images.zip';
                zipLink.click();
            });
        }
    });
}