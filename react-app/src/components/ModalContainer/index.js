import React, { useState } from "react";
import { InfoCard } from "../InfoCard";
import { Modal } from '../../context/Modal';

export const ModalContainer = () => {
  const [showModal, setShowModal] = useState(false);

  const showModalOnHover = (e) => {
    e.stopPropagation();
    setShowModal(true);
  };

  const hideModalOnHover = (e) => {
    e.stopPropagation();
    setShowModal(false);
  };
  return (
    <div style={{ maxWidth: "100%" }}>
      <button style={{ cursor: "pointer" }} onClick={() => setShowModal(!showModal)}>
        <i style={{ fontSize: "20px" }} className="fas fa-id-card"></i>
      </button>
      {showModal && (
        <Modal onClose={() => setShowModal(false)}>
          <InfoCard />
        </Modal>
      )}
      {showModal ? <InfoCard /> : null}
    </div>
  );
};

export default ModalContainer;