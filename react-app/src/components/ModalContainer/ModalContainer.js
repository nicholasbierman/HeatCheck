import React, { useState } from 'react';
import { Modal } from '../Modal/Modal';


export const ModalContainer = () => {
    const [ showModal, setShowModal ] = useState(false);

    const showModalOnHover = (e) => {
        e.stopPropagation()
        setShowModal(true)
    }

    const hideModalOnHover = (e) => {
        e.stopPropagation()
        setShowModal(false);
    }
    return (
        <div style={{maxWidth: "100%"}}>
            <button onMouseOver={(e) => showModalOnHover(e)}>About Me</button>
            {showModal ? <Modal /> : null}
        </div>

    )
}