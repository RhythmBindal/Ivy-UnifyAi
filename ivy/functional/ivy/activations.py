"""Collection of Ivy activation functions."""

from typing import Union, Optional

# local
import ivy
from ivy.framework_handler import current_framework as _cur_framework


# Extra #
# ------#


def relu(
    x: Union[ivy.Array, ivy.NativeArray],
    out: Optional[Union[ivy.Array, ivy.NativeArray]] = None,
) -> ivy.Array:
    """Applies the rectified linear unit function element-wise.

     Parameters
     ----------
     x
         input array
    out
        optional output array, for writing the result to. It must have a shape that the inputs broadcast to.

    Returns
     -------
    ret
       an array containing the rectified linear unit activation of each element in ``x``.

    Examples
    --------
    >>> x = ivy.array([-1., 0., 1.])
    >>> y = ivy.relu(x)
    >>> print(y)
    ivy.array([0., 0., 1.])

    """
    return _cur_framework(x).relu(x, out)


def leaky_relu(
    x: Union[ivy.Array, ivy.NativeArray], alpha: Optional[float] = 0.2
) -> ivy.Array:
    """Applies the leaky rectified linear unit function element-wise.

    Parameters
    ----------
    x
        Input array.
    alpha
        Negative slope for ReLU.

    Returns
    -------
    ivy.Array
        The input array with leaky relu applied element-wise.

    Examples:
    ---------
    >>> x = ivy.array([0.39, -0.85])
    >>> y = ivy.leaky_relu(x)
    >>> print(y)
    ivy.array([0.39, -0.17])

    """
    return _cur_framework(x).leaky_relu(x, alpha)


def gelu(x, approximate=True):
    """Applies the Gaussian error linear unit (GELU) activation function.

    Parameters
    ----------
    x
        Input array.
    approximate
        Whether to approximate, default is True.

    Returns
    -------
        The input array with leaky relu applied element-wise.

    """
    return _cur_framework(x).gelu(x, approximate)


def tanh(x: Union[ivy.Array, ivy.NativeArray]) -> ivy.Array:
    """Applies the Hyperbolic tangent activation function element-wise.

    Parameters
     ----------
    x
         input array

    Returns
    -------
    ret
        The input array with Hyperbolic tangent activation applied element-wise.

    Examples
    --------
    >>> x = ivy.array([0.55 , -0.55])
    >>> y = ivy.tanh(x)
    >>> print(y)
    ivy.array([0.50, -0.50])

    """
    return _cur_framework(x).tanh(x)


def sigmoid(x: Union[ivy.Array, ivy.NativeArray]) -> ivy.Array:
    """Applies the sigmoid function element-wise.

    Parameters
    ----------
    x
        input array.


    Returns
    -------
    ret
       an array containing the sigmoid activation of each element in ``x``.

    Examples
    --------
    >>> x = ivy.array([-1., 1., 2.])
    >>> y = ivy.sigmoid(x)
    >>> print(y)
    ivy.array([0.268, 0.5, 0.880])

    """
    return _cur_framework(x).sigmoid(x)


def softmax(
    x: Union[ivy.Array, ivy.NativeArray], axis: Optional[int] = -1
) -> ivy.Array:
    """Applies the softmax function element-wise.

    Parameters
    ----------
    x:
        Input array.
    axis:
        The dimension softmax would be performed on. The default is -1 which indicates the last dimension.

    Returns
    -------
    out:
        The input array with softmax applied element-wise.

    Examples:
    >>> x = ivy.array([-1.0, 0, 1.0])
    >>> y = ivy.softmax(x)
    >>> print(y)
    ivy.array([0.09003057, 0.24472847, 0.66524096])

    """
    return _cur_framework(x).softmax(x, axis)


def softplus(x: Union[ivy.Array, ivy.NativeArray]) -> ivy.Array:
    """Applies the softplus function element-wise.

    Parameters
    ----------
    x
        input array.

    Returns
    -------
        an array containing the softplus activation of each element in ``x``.
    Examples:
    ---------
    >>> x = ivy.array([-0.3461, -0.6491])
    >>> y = ivy.softplus(x)
    >>> print(y)
    ivy.array([0.5350, 0.4203])

    """
    return _cur_framework(x).softplus(x)