# Image-Compressor-SVD
A simple Python program that uses Linear Algebra techniques, namely, Singular Value Decomposition, to compress an image file.
Singular Value Decomposition (SVD) is a matrix factorization technique (such as the LU or QR factorizations) that can be applied to any real matrix $A \in \mathbb{R}_{m\times n}$. An example:

<figure>
  <img src="imgs/im1.jpg" alt="imagen 1" style="width:75%;">
  <figcaption><i>Uncompressed image (956KB)</i></figcaption>
</figure>

<figure>
  <img src="imgs/im2.jpg" alt="imagen 2" style="width:75%;">
  <figcaption><i>Compressed image using k=150 of a total of 2160 singular values. (521KB)</i></figcaption>
</figure>
<br/><br/>
We should remark that this is obviously <b>not the best compression method</b> that exists. This is just a <b>cool application of linear algebra</b> in computer science.
<br/><br/>
The SVD factorizes $A$ into three matrices: an orthogonal matrix $U \in \mathbb{R}\_{m\times m}$, a diagonal matrix $Σ \in\mathbb{R}\_{m\times n}$ and another orthogonal matrix $V \in \mathbb{R}\_{n\times n}$. The SVD allows us to compute A in terms of these matrices: $$A = UΣV^{T}.$$

The columns $(u\_{1}, u\_{2}, ...,u\_{m})$ of $U$ form an orthonormal basis for $\mathbb{R}^{m}$, the matrix $\Sigma$ contains the singular values of $A$ and the columns $(v\_{1}, v\_{2}, ...,v\_{n})$ of $V$ form an orthonormal basis for $\mathbb{R}^{n}$.

The singular values of A are defined as follows: Let $\lambda_{1} \geq \lambda_{2} \geq ... \geq \lambda_{r} \gt 0$ with $r \leq n$ be the positive eigenvalues of $(A^{T}A)\_{n\times n}$. We say that $\sigma\_{i} = \sqrt{\lambda\_{i}} \gt 0$ is the i-th singular value of $A$, for $i=1, 2, ..., r$. Thus $\Sigma=diag\_{m\times n}(\sigma\_{1}, \sigma\_{2}, ..., \sigma\_{r})$.

It can be proven (by using the block representation of matrix product) that $$A = \sigma\_{1}u\_{1}v^{T}\_{1} + \sigma\_{2}u\_{2}v^{T}\_{2} + ... + \sigma\_{r}u\_{r}v^{T}\_{r}.$$

This is known as the <b>outer product form of the SVD </b> and it allows us to see our matrix $A$ reduced to its most fundamental components.<br/> What each term contributes to the original matrix $A$ is determined by the singular value that multiplies it. Since $\sigma\_{1} \geq \sigma\_{2} \geq ... \geq \sigma\_{r} \gt 0,$ the first terms give us way more information about $A$ than the last terms of the sum.
So we can keep only a few of the first terms and discard the rest: this way we are preserving the majority of information that $A$ contains and removing irrelevant data that could take up memory space and cause poor performance.

In relation to image compressing, we can treat an image as an $m\times n$ matrix, being $m$ the height of the image and $n$ the width, whose entries represent pixels.
In general, each pixel is represented by 1 byte, or 8 bits, which represent a color value from 0 to 255.

By using SVD we can reduce the amount of bytes needed to accurately represent an image.
